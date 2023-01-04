#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
#include <Psapi.h>

/*****************************************************************/
/*                          IMPORTANT                            */
/* You can change any part of the skeleton (even the signatures) */
/* There are 4 TODOs in the skeleton. Follow them in order       */
/*****************************************************************/

// The maximum number of processes
#define MAX_NUM_PROCESSES 1024

// Use this to crash to check if malloc failed
static inline void exitWithErrorNoMemory(PVOID assertVal)
{
    if (!assertVal) {
        printf("Not enough memory, exiting...\n");
        ExitProcess(ENOMEM);
    }
}

static DWORD retrieveProcesses(PDWORD *processesIdArray, DWORD arraySize)
{
    DWORD lpcbNeeded;

    // DONE 2: Fill processesIdArray with available processes
    // DONE 2: Return the number of entries returned by the function
    // Hint: Call EnumProcesses
    EnumProcesses(*processesIdArray, arraySize, &lpcbNeeded);

    return lpcbNeeded / sizeof(DWORD);
}

static HANDLE openProcess(DWORD processId)
{
    return OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);
}

static void closeProcessList(PHANDLE processHandles, DWORD handleArraySize)
{
    for (DWORD i = 0; i < handleArraySize; ++i) {
        CloseHandle(processHandles[i]);
    }
}

static DWORD processesToHandles(PHANDLE handleArray)
{
    PDWORD processIdArray = (PDWORD) malloc(MAX_NUM_PROCESSES * sizeof(DWORD));
    DWORD processIdSize;
    HANDLE currentHandle;
    DWORD openHandles = 0;
    exitWithErrorNoMemory(processIdArray);

    // DONE 3: Retrieve all processes using the retrieveProcesses function
    DWORD sz = retrieveProcesses((PDWORD*)&processIdArray, MAX_NUM_PROCESSES * sizeof(DWORD));
    // DONE 3: Open all process ids (that are positive) with the openProcess function
    // Hint: If the returned handle is > 0, the opening succeeded
    for (int i = 0; i < sz; i++) {
        HANDLE hdl = openProcess(processIdArray[i]);
        if (hdl != NULL) {
            handleArray[openHandles] = hdl;
            openHandles++;
        }
    }

    // DONE 3: Return the number of open handles
    free(processIdArray);
    return openHandles;
}

static void getMemoryInfoForHandles(PHANDLE handleArray, PPROCESS_MEMORY_COUNTERS counters, DWORD processArraySize)
{
    // DONE 4: Retrieve the memory information for each process in the processArray and fill the data into counters
    // Hint: Call GetProcessMemoryInfo

    for (int i = 0; i < processArraySize; i++) {
        bool res = GetProcessMemoryInfo(handleArray[i], &counters[i], sizeof(counters[i]));
    }
}

static PCHAR *getProcessNameForHandles(PHANDLE processArray, DWORD processArraySize)
{
    PCHAR *paths = (PCHAR *) malloc(processArraySize * sizeof(*paths));
    DWORD size = MAX_PATH;
    exitWithErrorNoMemory(paths);

    for (DWORD i = 0; i < processArraySize; ++i) {
        paths[i] = (PCHAR) malloc(MAX_PATH * sizeof(**paths));
        exitWithErrorNoMemory(paths[i]);
        size = MAX_PATH;
        QueryFullProcessImageNameA(processArray[i], PROCESS_NAME_NATIVE, paths[i], &size);
    }

    return paths;
}

static PERFORMANCE_INFORMATION getSystemInfo()
{
    PERFORMACE_INFORMATION perf = { 0, };
    // DONE 1: retrieve performance information from the system
    // Hint: Call GetPerformanceInfo

    GetPerformanceInfo(&perf, sizeof(perf));
    return perf;
}

// Helper: Parses the full path to extract only the executable
static int extractExecutable(PCHAR pathName)
{
    for (int i = strlen(pathName) - 1; i >= 0; --i) {
        if (pathName[i] == '\\') {
            return i + 1;
        }
    }
    return 0;
}

// Prints all data regarding performance
static void printSystemInfo(PERFORMANCE_INFORMATION perfInfo)
{
    printf("CommitTotal, CommitLimit, CommitPeak, PhysicalTotal, PhysicalAvailable, SystemCache, "
        "KernelTotal, KernelPaged, KernelNonpaged, PageSize, HandleCount, ProcessCount, ThreadCount\n");
    printf("%lld, %lld, %lld, %lld, %lld, %lld, %lld, %lld, %lld, %lld, %lu, %lu, %lu\n\n",
        perfInfo.CommitTotal,
        perfInfo.CommitLimit,
        perfInfo.CommitPeak,
        perfInfo.PhysicalTotal,
        perfInfo.PhysicalAvailable,
        perfInfo.SystemCache,
        perfInfo.KernelTotal,
        perfInfo.KernelPaged,
        perfInfo.KernelNonpaged,
        perfInfo.PageSize,
        perfInfo.HandleCount,
        perfInfo.ProcessCount,
        perfInfo.ThreadCount
        );
}

// Prints all data regarding memory for each process and its name
static void printTableInfo(PPROCESS_MEMORY_COUNTERS memoryCounterData, PCHAR *processNames, DWORD counterSize)
{
    printf("ProcessName, PageFaultCount, PeakWorkingSetSize, WorkingSetSize, QuotaPeakPagedPoolUsage, QuotaPagedPoolUsage, "
            "QuotaPeakNonPagedPoolUsage, QuotaNonPagedPoolUsage, PagefileUsage, PeakPagefileUsage\n");

    for (DWORD i = 0; i < counterSize; ++i) {
        printf("%s, %lu, %lld, %lld, %lld, %lld, %lld, %lld, %lld, %lld\n",
            processNames[i] + extractExecutable(processNames[i]),
            memoryCounterData[i].PageFaultCount,
            memoryCounterData[i].PeakWorkingSetSize / 1024,
            memoryCounterData[i].WorkingSetSize / 1024,
            memoryCounterData[i].QuotaPeakPagedPoolUsage / 1024,
            memoryCounterData[i].QuotaPagedPoolUsage / 1024,
            memoryCounterData[i].QuotaPeakNonPagedPoolUsage / 1024,
            memoryCounterData[i].QuotaNonPagedPoolUsage / 1024,
            memoryCounterData[i].PagefileUsage / 1024,
            memoryCounterData[i].PeakPagefileUsage / 1024
            );
    }
}

static void initEnvironment(PHANDLE *handleArray)
{
    *handleArray = (PHANDLE) malloc(MAX_NUM_PROCESSES * sizeof(**handleArray));
}

static void cleanupEnvironment(PHANDLE handleArray, PPROCESS_MEMORY_COUNTERS memoryCounterData, PCHAR *processNames, DWORD openProcesses)
{
    for (DWORD i = 0; i < openProcesses; ++i) {
        CloseHandle(handleArray[i]);
        free(processNames[i]);
    }
    free(handleArray);
    free(memoryCounterData);
    free(processNames);
}

int main()
{
    PHANDLE handleArray;
    DWORD openProcesses;
    PPROCESS_MEMORY_COUNTERS memoryCounterData;
    PERFORMANCE_INFORMATION perfInfo;
    PCHAR *processNames;

    initEnvironment(&handleArray);
    openProcesses = processesToHandles(handleArray);
    memoryCounterData = (PPROCESS_MEMORY_COUNTERS) calloc(openProcesses, sizeof(PROCESS_MEMORY_COUNTERS));
    exitWithErrorNoMemory(memoryCounterData);

    getMemoryInfoForHandles(handleArray, memoryCounterData, openProcesses);
    processNames = getProcessNameForHandles(handleArray, openProcesses);
    perfInfo = getSystemInfo();
    printSystemInfo(perfInfo);
    printTableInfo(memoryCounterData, processNames, openProcesses);
    cleanupEnvironment(handleArray, memoryCounterData, processNames, openProcesses);
    return 0;
}

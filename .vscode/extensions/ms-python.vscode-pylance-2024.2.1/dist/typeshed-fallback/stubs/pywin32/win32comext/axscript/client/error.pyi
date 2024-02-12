from win32com.server.exception import COMException

debugging: int

def FormatForAX(text): ...
def ExpandTabs(text): ...
def AddCR(text): ...

class IActiveScriptError:
    def GetSourceLineText(self): ...
    def GetSourcePosition(self): ...
    def GetExceptionInfo(self): ...

class AXScriptException(COMException):
    sourceContext: int
    startLineNo: int
    linetext: str
    def __init__(self, site, codeBlock, exc_type, exc_value, exc_traceback) -> None: ...
    def ExtractTracebackInfo(self, tb, site): ...

def ProcessAXScriptException(scriptingSite, debugManager, exceptionInstance): ...

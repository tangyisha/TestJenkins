'''
exmaple cmdline invocation:
mitmdump --rawtcp --tcp-host ".*" -s examles/complex/tcp_message.py
'''
from mitmproxy.utils import strutils
from mitmproxy import ctx
from mitmproxy import tcp

def tcp_message(flow: tcp.TCPFlow):
    message = flow.messages[-1]
    old_content = message.content
    # 将原来tcp内容中的foo替换成bar
    # message.content = old_content.replace(b"foo", b"bar")
    # 我们需要把grep -a @webview_devtools_remote_替换成grep -a _devtools_remote_，查看小程序的进程
    message.content = old_content.replace(b"grep -a @webview_devtools_remote_", b"grep -a _devtools_remote_")

    # 日志输出
    ctx.log.info(
        "[tcp_message()] from {} to {}:\n{}".format(
            "(modified)" if message.content != old_content else "",
            "clinet" if message.from_client else "server",
            "server" if message.from_client else "client"
        )
    )
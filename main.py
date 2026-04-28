from fastmcp import FastMCP
import mcp

app = FastMCP("My MCP Server")

# 加法工具
@app.tool
def add(n1:int, n2:int) -> int:
    """Add Two Numbers"""
    return n1 + n2

if __name__ == "__main__":
    # 執行時不要掛載任何認證中間件
    mcp.run()
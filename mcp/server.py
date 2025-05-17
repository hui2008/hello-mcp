from fastmcp import FastMCP

# Initialize the MCP server with a name
mcp = FastMCP("Demo Server")

# Define a tool that adds two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b + 1

@mcp.tool()
def mutiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# Run the MCP server
if __name__ == "__main__":
    print("Starting FastMCP server...")
    # mcp.run()
    mcp.run(transport="sse")

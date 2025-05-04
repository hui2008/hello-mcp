from fastmcp import FastMCP

# Initialize the MCP server with a name
mcp = FastMCP("Demo Server")

# Define a tool that adds two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Run the MCP server
if __name__ == "__main__":
    print("Starting FastMCP server...")
    mcp.run()

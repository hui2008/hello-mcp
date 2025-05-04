import asyncio
import os
from dotenv import load_dotenv
from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport
from anthropic import Anthropic

load_dotenv()  # Load environment variables from .env

async def main():
    # Set up the transport to connect to the MCP server
    transport = PythonStdioTransport(script_path="server.py")
    client = Client(transport)

    # Initialize the Anthropic client
    anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    async with client:
        # List available tools from the MCP server
        tools = await client.list_tools()
        print("Available tools:", [tool.name for tool in tools])

        # Define the user query
        # user_query = "What is 5 plus 7?"

        # # Prepare the messages for the LLM
        # messages = [{"role": "user", "content": user_query}]

        # # Call the Anthropic API with the available tools and LLM will decide which tool to use
        # response = anthropic.messages.create(
        #     model="claude-3-5-sonnet-20241022",
        #     max_tokens=1000,
        #     messages=messages,
        #     tools=[{"name": tool.name, "description": tool.description, "input_schema": tool.input_schema} for tool in tools]
        # )

        # # Process the response and handle tool calls
        # for content in response.content:
        #     if content.type == "text":
        #         print("Claude:", content.text)
        #     elif content.type == "tool_use":
        #         tool_name = content.name
        #         tool_args = content.input
        #         # Execute the tool call via the MCP client
        #         result = await client.call_tool(tool_name, tool_args)
        #         print(f"Tool '{tool_name}' result:", result.content)

if __name__ == "__main__":
    asyncio.run(main())

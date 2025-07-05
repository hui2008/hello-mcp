##

```mermaid
sequenceDiagram
participant host
participant client
participant server
participant LLM

host ->> LLM: reasoning/planing
host ->> client:call mcp tools
client ->> server: sampling/createMessage
server ->> client: push
client ->> LLM: completion
```
# VeraTemple
An agentic framework for the VeraDSL agent composition language.

## Setup
### Python Env

Using ``uv`` at the root of project, run:

```bash
uv run sync
```

### LLM Env (On-Device)

Download and install [Ollama](https://ollama.com/download).

As an initial model, use ``llama3.2``.

Once Ollama is downloaded and installed, from the command line run:

```bash
ollama pull llama3.2
```

To confirm once the pull finishes, run:

```bash
ollama list
```

And should see something like:

```bash
NAME               ID              SIZE      MODIFIED     
llama3.2:latest    a80c4f17acd5    2.0 GB    1 second ago
```

Now run this curl command to invoke Ollama’s OpenAI compatible API endpoint:

```bash
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "llama2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```

> <b>Note</b>: This is necessary b/c we are currently using fast-agent as a dependency and it depends on OpenAI compatible API endpoints.

## Testing

Go to ``examples/conversational-agent`` and run:

```bash
uv run agent.py
```

You should have an active conversation running with an agent in the terminal.

If you want to test other models from the Ollama model repository hub you'll just need to modify:

```yaml
default_model: generic.llama3.2
```
In the ``fastagent.config.yaml`` file.

Make sure ``generic.`` is prepended before the model name.
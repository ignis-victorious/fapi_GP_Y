# fapi_GP_Y

A project created with FastAPI CLI.

## Quick Start

### Start the development server:

```bash
uv run fastapi dev
```

Visit http://localhost:8000

### Deploy to FastAPI Cloud:

> Reader's note: These commands are not quite ready for prime time yet, but will be soon! Join the waiting list at https://fastapicloud.com!

```bash
uv run fastapi login
uv run fastapi deploy
```

## Project Structure

- `main.py` - Your FastAPI application
- `pyproject.toml` - Project dependencies

## Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [FastAPI Cloud](https://fastapicloud.com)

## Describe the entrypoint to FastAPI:

- Add to src/   
`__init__.py `  

- Add to pyproject.toml   
`[tool.fastapi]`        
`entrypoint="src:app"` 

where app is the FastAPI() instance, i.e. app = FastAPI()

## Adapted for educational purposes from:

[Setting up our FastAPI App 🚀 | Let’s Learn FastAPI Together! Garima Paudel](https://www.youtube.com/watch?v=aKxZCyNtgRw)
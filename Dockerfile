# ---------- Builder Stage ----------
FROM python:3.13-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*
        
# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
        
WORKDIR /app
        
# Copy dependency files
COPY pyproject.toml uv.lock ./

# Copy alembic.ini
COPY alembic.ini ./
    
# Install dependencies (excluding dev dependencies)
RUN uv venv && \
    uv sync --frozen --no-dev --no-editable
        
# Copy application code
COPY ./app ./app
        
# ---------- Final Stage ----------
FROM python:3.13-slim AS final
        
# Install runtime dependencies (e.g., for asyncpg)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
        
# Create a non-root user
RUN useradd -m appuser
        
WORKDIR /app
        
# Copy installed virtualenv and application code
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/app ./app
COPY --from=builder /app/alembic.ini /app/alembic.ini
        
# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/.venv"
        
# Change ownership to non-root user
RUN chown -R appuser:appuser /app
        
# Switch to non-root user
USER appuser
    
ARG APP_HOST
ARG APP_PORT
ENV APP_HOST=${APP_HOST}
ENV APP_PORT=${APP_PORT}
            
CMD ["sh", "-c", "uvicorn app.main:app --host ${APP_HOST} --port ${APP_PORT}"]
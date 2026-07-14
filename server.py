from __future__ import annotations

import argparse
from datetime import datetime, timezone
from typing import Any

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    name="Enterprise Cloud MCP",
    host="127.0.0.1",
    port=8000,
    stateless_http=True,
    json_response=True,
)


@mcp.tool()
def health_check() -> dict[str, Any]:
    """Comprueba que el servidor MCP está funcionando."""

    return {
        "status": "ok",
        "service": "enterprise-cloud-mcp",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }


@mcp.tool()
def add(a: float, b: float) -> dict[str, float]:
    """Suma dos números."""

    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@mcp.tool()
def cloud_architecture() -> dict[str, Any]:
    """Devuelve una arquitectura AWS de detección de fraude."""

    return {
        "name": "Real-Time Fraud Detection Platform",
        "cloud": "AWS",
        "components": [
            "Amazon API Gateway",
            "Amazon Kinesis Data Streams",
            "AWS Lambda",
            "Amazon SageMaker",
            "Amazon SQS",
            "Amazon S3",
            "Amazon RDS",
            "Amazon CloudWatch",
        ],
        "data_flow": [
            "API Gateway recibe la transacción.",
            "Kinesis ingiere el evento.",
            "Lambda valida y enriquece la información.",
            "SageMaker calcula el riesgo.",
            "SQS desacopla operaciones sospechosas.",
            "RDS y S3 almacenan los resultados.",
            "CloudWatch registra logs, métricas y alertas.",
        ],
    }


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--transport",
        choices=["stdio", "streamable-http"],
        default="streamable-http",
    )

    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    mcp.run(transport=arguments.transport)


if __name__ == "__main__":
    main()
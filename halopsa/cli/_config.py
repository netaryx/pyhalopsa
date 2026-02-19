"""Config file loading and credential resolution."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

CONFIG_DIR = Path.home() / ".halopsa"
CONFIG_FILE = CONFIG_DIR / "config.yaml"


@dataclass
class HaloConfig:
    """Resolved configuration for the HaloPSA client."""

    tenant_url: str = ""
    client_id: str = ""
    client_secret: str = ""
    scope: str = "all"
    tenant: str | None = None

    @property
    def is_complete(self) -> bool:
        return bool(self.tenant_url and self.client_id and self.client_secret)


def _load_config_file() -> dict[str, Any]:
    """Load config from ~/.halopsa/config.yaml if it exists."""
    if not CONFIG_FILE.exists():
        return {}
    try:
        import yaml

        with open(CONFIG_FILE) as f:
            data = yaml.safe_load(f) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def resolve_config(
    *,
    tenant_url: str | None = None,
    client_id: str | None = None,
    client_secret: str | None = None,
) -> HaloConfig:
    """Resolve credentials: CLI flags > env vars > config file."""
    file_cfg = _load_config_file()

    cfg = HaloConfig(
        tenant_url=(
            tenant_url
            or os.environ.get("HALO_TENANT_URL")
            or file_cfg.get("tenant_url", "")
        ),
        client_id=(
            client_id
            or os.environ.get("HALO_CLIENT_ID")
            or file_cfg.get("client_id", "")
        ),
        client_secret=(
            client_secret
            or os.environ.get("HALO_CLIENT_SECRET")
            or file_cfg.get("client_secret", "")
        ),
        scope=file_cfg.get("scope", "all"),
        tenant=file_cfg.get("tenant"),
    )
    return cfg


def save_config(data: dict[str, Any]) -> Path:
    """Write config to ~/.halopsa/config.yaml."""
    import yaml

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(data, f, default_flow_style=False)
    CONFIG_FILE.chmod(0o600)
    return CONFIG_FILE

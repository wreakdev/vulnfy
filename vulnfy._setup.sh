#!/bin/bash
VULNFY="vulnfy.py"
VULNFY_ALIAS="vulnfy"
chmod +x "$VULNFY"
cp "$VULNFY" "$HOME/.local/bin/$VULNFY_ALIAS"

echo "[+] Vulnfy installed."
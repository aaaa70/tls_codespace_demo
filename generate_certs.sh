#!/bin/bash
set -e
CERT="cert.pem"
KEY="key.pem"
if [ -f "$CERT" ] || [ -f "$KEY" ]; then
  echo "cert.pem یا key.pem قبلاً وجود دارد — بازنویسی نمی‌شود."
  exit 0
fi
openssl req -x509 -nodes -newkey rsa:2048           -keyout "$KEY" -out "$CERT" -days 365           -subj "/CN=localhost"
echo "گواهی و کلید ساخته شد: $CERT , $KEY"

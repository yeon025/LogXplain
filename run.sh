#!/bin/bash
set -e

ARCHIVE="pkl.zip"
TARGET_DIR="project"
PKL_DIR="$TARGET_DIR/pkl"

if [ -d "$PKL_DIR" ]; then
    echo "[INFO] $PKL_DIR 폴더가 이미 존재합니다. 압축 해제 건너뜀."
else
    echo "[INFO] $PKL_DIR 폴더가 없어 압축 해제 진행."
    unzip -q "$ARCHIVE" -d "$TARGET_DIR"
fi

cd "$TARGET_DIR"
echo "[INFO] Docker Compose 백그라운드 실행"
docker-compose up -d

echo "[INFO] 로그 출력"
docker-compose logs -f
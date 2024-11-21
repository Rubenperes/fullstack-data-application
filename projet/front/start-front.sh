#!/bin/bash

echo "SSL"
npm config set strict-ssl false

echo "npm install"
npm install

echo "verif vite"
npm list vite

echo  "run dev"
npm run dev
# Peminjaman Alat

Proyek Cloud Computing Week 12, Track A (EC2 + RDS MySQL).

## Entity
equipment: id, name, status, borrower

## Rencana Endpoint
- POST /equipment
- GET /equipment/{id}
- PUT /equipment/{id}
- DELETE /equipment/{id}

## Deployment Plan
1. Siapkan VPC dan security group
2. Buat RDS MySQL (private)
3. Buat EC2 (Amazon Linux 2023)
4. Jalankan schema.sql
5. Jalankan app.py
6. Tes GET /health

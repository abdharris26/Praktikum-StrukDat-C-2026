tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

irisan = tim_frontend.intersection(tim_backend)

print("irisan:",irisan)

backend_only = tim_backend.difference(tim_frontend)
print("backend aja:",backend_only)

gabungan = tim_frontend | tim_backend

print("total keahlian:",gabungan)

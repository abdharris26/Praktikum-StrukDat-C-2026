tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

#1 tentukan irisannya(keahlian yang dimiliki kedua tim)
irisan = tim_frontend.intersection(tim_backend)

print("irisan:",irisan)

#2 keahlian yang dimiliki tim tim_backend
backend_only = tim_backend.difference(tim_frontend)
print("backend aja:",backend_only)

#3 gabungan seluruh keahlian
gabungan = tim_frontend | tim_backend

print("total keahlian:",gabungan)

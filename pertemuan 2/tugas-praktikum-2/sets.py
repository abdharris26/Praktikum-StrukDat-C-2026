tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

irisan = tim_frontend.intersection(tim_backend)

print("irisan:",irisan)

backend_only = tim_backend.difference(tim_frontend)
print("backend aja:",backend_only)

gabungan = tim_frontend | tim_backend

print("total keahlian:",gabungan)


buah = {"apple", "banana", "cherry"}

print(buah)

buah.add("orange")

buah.remove("banana")

print(buah)

buah_lain = {"mango", "apple"}

gabungan = buah.union(buah_lain)
irisan = buah.intersection(buah_lain)

print("Gabungan:", gabungan)
print("Irisan:", irisan)

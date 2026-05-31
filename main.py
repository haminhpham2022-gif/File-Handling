file = open("bucketlist.txt", "w")
file.write("travel around the world during a gap year \nget my drivers license before 20 \nsee my favorite artists live \nget a mini-job for experience \nvisit a tropical area")
file.close()

file = open("bucketlist.txt", "a")
file.write("climb a mountain \nsee wild animals (a tiger or lion maybe) \ngo diving \nhave holiday on a cruise ship \nadopt a pet when i live alone \nlearn the basics of skateboarding")
file.close()

print("Bucket-List created successfully!")

file = open("bucketlist.txt", "r")
lines = file.readlines()
count = len(lines)
print(f"you have {count} items on your bucket list")
file.close()

file = open("bucketlist.txt", "r")
content = file.read()
print(content)
file.close()
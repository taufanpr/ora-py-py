# Fungsi IF bisa digunakan bertingkat. 
# Atau dilakukan pengecekan lebih dari 1 statement di dalamnya.


#  if ( i<7 && i <3)

# artinya i harus bernilai kurang dari 7 dan kurang dari 3 agar bisa memenuhi pengecekan.


# Bisa juga dilakukan pengecekan bertingkat:


i=2
if (i<7):
        print("nilai i kurang dari 7")
        if (i<3):
                print("nilai i kurang dari 7 dan kurang dari 3")
        else:
                print("nilai i kurang dari 7 tapi lebih dari 3")



# hasil:

# nilai i kurang dari 7
# nilai i kurang dari 7 dan kurang dari 3
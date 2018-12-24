#Stephen Duncanson
#Stephen@stephlog.com
#December 24, 2018

#I'll need to import time to keep track of rest times and all that.
import time

#I'll need this to save each workout as a specific date
import datetime
today = str(datetime.date.today())

def warmup():
    print("***WARMUP***")
    print("1. Prying goblet squat x5")
    time.sleep(5)
    input("Press enter when finished...")
    print("2. 3 second glute bridges x5")
    time.sleep(5)
    input("Press enter when finished...")
    print("3. Kettlebell halos, both ways x5")
    time.sleep(5)
    input("Press enter when finished...")


def workout():
    print("***WORKOUT***")
    workout_log = open("workout_log.txt", "a")
    workout_log.write(today + "\t")
    start = time.time()
    time.sleep(60)
    print("okay!")
    end = time.time()
    total_time = (end - start)/60
    total_time = str(format(total_time, ".2f"))
    workout_log.write(total_time)
    workout_log.write(" minutes\t")
    workout_log.close()

def cooldown():
    print("***STRETCHING***")
    #Starting stretching
    print()


def main():
    print("Welcome to Stephen's Simple AND Sinister (SSANDS)!")
    option = ""
    while option != "w" or "h" or "i" or "q":
        print("(w)orkout\t(h)istory\t(i)nfo\t(q)uit")
        option = input(">")
        if option == "w":
            warmup()
            workout()
            cooldown()
            quit()
        if option == "h":
            print("Under construction!")
            #open the file in a read mode and print stats
        if option == "i":
            print("Made by Stephen\nStephen@stephlog.com\n2018")
        if option == "q":
            quit()


main()

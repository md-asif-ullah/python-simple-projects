import json

file_name ="youtube.txt"


def save_data_helper(videos):
    with open(file_name,"w") as file:
        json.dump(videos,file)

def load_data():
    try:
        with open(file_name,"r") as file:
         return  json.load(file)
    except FileNotFoundError:
         return []

def list_all_videos(videos):
    print("-"*50)
    print("\n")
    print("videos:")
    print("\n")
    for index,videos in enumerate(videos,start=1):
        print(f"{index}. video name is {videos["name"]} video duration is {videos["time"]}min")

    print("\n")
    print("-"*50)

def add_video(videos):
    video_name = input("enter your video name: ")
    video_time=input("enter your video time: ")
    videos.append({"name":video_name ,"time":video_time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index= int(input("enter the video number to update: "))
  
    if index >= 1 and index < len(videos) :
        newName= input("enter the new video name")
        newTime=input("enter the new video time")
        videos[index-1]={"name" :newName ,"time" :newTime}
        save_data_helper(videos)

        print(f"{index} number video update successfully")
    else :
        print("invalid index selected")

def delete_videos (videos):
    list_all_videos(videos)        
    index=int(input('enter video index to delete: '))
    print(type(index))

    if index >= 1 and index < len(videos) :
       
       del videos[index-1]
       save_data_helper(videos)
       print(f"{index} number video deleted successfully")
    else :
        print("invalid index selected")



videos=load_data()

def main():
    while True:
        print("\n youtube manager | choose an option ")
        print("1. list a favourite videos ")
        print("2. add a youtube video")
        print("3. update a youtube video")
        print("4. delete a youtube video")

        choice =input("enter your choice:")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_videos(videos)
            
            case _:
                print("invalid choice")
           

if __name__=="__main__":
    main()
import Helper

mbrsHlpr = Helper.MembersManager()
mbrsHlpr.create_member("Mohammed", 31)
mbrsHlpr.create_member("Ahmed",25)
mbrsHlpr.create_member("Ismail",19)
mbrsHlpr.get_all_members()


postsHlpr = Helper.PostsManager()
postsHlpr.create_post("post1","this is my first post")
postsHlpr.create_post("post2","this my second post")
postsHlpr.create_post("post3","this is my third post")
postsHlpr.get_all_posts()
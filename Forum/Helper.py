import models

class MembersManager:
    members = []

    def create_member(self,name,age):
        member = models.Member(name,age)
        self.members.append(member)  

    def add_member(self,member):
        self.members.append(member)  

    def get_all_members(self):
        for member in self.members:
            print "Name: {0} || Age: {1}".format(member.name,member.age)           



class PostsManager:
	posts = []

	def create_post(self,title,content):
		post = models.Post(title,content)
		self.posts.append(post)	

	def add_post(self,post):
		self.posts.append(post)

	def get_all_posts(self) :       
          for post in self.posts:
            print "Post:{0} || content:{1}".format(post.title,post.content)	 	

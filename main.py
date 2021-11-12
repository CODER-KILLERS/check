import requests as req,re
from bs4 import BeautifulSoup as par

#data - data
data,data2={},{}
aman,cp,salah=0,0,0

class Main(object):
	
	def __init__(self,url,user,pw):
		self.url = url
		self.user = user
		self.pw = pw
	def banner(self):
		logo="""
	
   ______     __      ____             _ 
  / ____/__  / /__   / __ \____  _____(_)
 / /   / _ \/ //_/  / / / / __ \/ ___/ / Coded By: Latip176
/ /___/  __/ ,<    / /_/ / /_/ (__  ) / https://latip176.my.id
\____/\___/_/|_|   \____/ .___/____/_/   
                       /_/               
	Cek Opsi Checkpoint Facebook
	"""
		return logo
		

class Eksekusi(Main):
	
	def cek_opsi(self):
		global aman,cp,salah
		session=req.Session()
		session.headers.update({
			"Host":"mbasic.facebook.com",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-encoding":"gzip, deflate",
			"accept-language":"id-ID,id;q=0.9",
			"referer":"https://mbasic.facebook.com/",
			"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
		})
		soup=par(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
		link=soup.find("form",{"method":"post"})
		for x in soup("input"):
			data.update({x.get("name"):x.get("value")})
		data.update({"email":self.user,"pass":self.pw})
		urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
		response=par(urlPost.text, "html.parser")
		if urlPost.status_code=="429":
			print("[!] Nyalakan lalu matikan mode pesawat 2 Detik")
		if "c_user" in session.cookies.get_dict():
			aman+=1
			print(f"\r[√] Akun aman\n[=] {self.user} | {self.pw}					\n\n")
		elif "checkpoint" in session.cookies.get_dict():
			cp+=1
			listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
			link2=response.find("form",{"method":"post"})
			for x in response("input"):
				if x.get("name") in listInput:
					data2.update({x.get("name"):x.get("value")})
			response2=par(session.post("https://mbasic.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
			number=0
			for cek in response2.find_all("option"):
				if(len(cek)>0):
					number+=1
					opsi=re.findall('\<option selected=\".+\" value=\".+\">(.+)<\/option>',str(cek))
					print(f"\r[×] Akun checkpoint\n[=] {self.user} | {self.pw}\n[!] Terdapat {len(cek)} opsi: \n[{number}]. {''.join(opsi)}							\n\n",end="")
				else:
					if "c_user" in session.cookies.get_dict():
						cp-=1
						aman+=1
						print(f"\r[√] Akun aman\n[=] {self.user} | {self.pw}				\n\n",end="")
					else:
						if "Apakah Ini Anda?" in str(cek):
							print("\r[√] Akun tap yes\n[=] {self.user} | {self.pw}							\n\n",end="")
					
		else:
			salah+=1
			print("\r[!] Kata sandi salah atau sudah diubah				\n\n")

def menu():
	print("[1]. Cek opsi satu persatu\n[2]. Cek opsi melalui file\n[!]. Note: di tengah username dan password\n     harus ada tanda '|' atau '•'\n")
	_pilih=input("[+] Chosee: ")
	while _pilih not in ("01","1","02","2"):
		print("\n[!] Pilihan tidak ada")
		_pilih=input("[+] Chosee: ")
	if(_pilih in ("01","1")):
		print("\n[!] Masukan username|password\n    contoh: latip|176")
		__data=input("[+] Masukan username|password: ")
		if "•" in __data:
			user,pw=__data.split("•")
		elif "|" in __data:
			user,pw=__data.split("|")
		else:
			exit("\n[!] Sertakan tanda | atau • ditengah username dan password\n")
		print(f"{'='*45}\n")
		Main = Eksekusi("https://mbasic.facebook.com",user,pw)
		Main.cek_opsi()
	elif(_pilih in ("02","2")):
		print("\n[!]. Masukan nama file dan baca\n     terlebih dahulu note di atas")
		__data=input("[+] Masukan nama file: ")
		try:
			_file=open(__data,"r").readlines()
		except FileNotFoundError:
			exit("[!] File tidak ditemukan")
		print("[✓] Jumlah akun:",len(_file),f"\n{'='*45}\n")
		for x in _file:
			if "•" in x:
				user,pw=x.split("•")
			elif "|" in x:
				user,pw=x.split("|")
			else:
				exit("\n[!] Tidak tersedia tanda | •\n")
			Eksekusi("https://mbasic.facebook.com",user.replace("\n",""),pw.replace("\n","")).cek_opsi()
		exit(f" *** Cek akun selesai hasil: \n [+] OK/CP/SALAH: {str(aman)}/{str(cp)}/{str(salah)}\n")
	
if __name__=="__main__":
	print(Eksekusi("","","").banner())
	menu()
						
		

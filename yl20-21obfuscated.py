import tkinter as a,base64 as b,sqlite3 as c,subprocess as d,sys as e,os as f
from tkinter import ttk as g,messagebox as h

x=lambda s:b.b64decode(s).decode()

A=x("dGtzcWx5bDE5dmlzdC5weQ==")
B=x("QXRhbW1lcy5kYg==")

C={
x("cm9vbXM="):(x("cm9vbV9udW1iZXI="),x("dHlwZQ=="),x("cHJpY2U="),x("YXZhaWxhYmxl")),
x("Ym9va2luZ3M="):(x("cm9vbXNfaWQ="),x("dXNlcnNfaWQ="),x("Y2hlY2tpbg=="),x("Y2hlY2tvdXQ=")),
x("cGF5bWVudHM="):(x("Ym9va2luZ19pZA=="),x("YW1vdW50"),x("cGF5bWVudF9kYXRl"),x("bWV0aG9k")),
x("dXNlcnM="):(x("Zmlyc3RfbmFtZQ=="),x("bGFzdF9uYW1l"),x("ZW1haWw="),x("cGhvbmU="),x("aW1hZ2U="))
}

D=list(C.keys())

def E():d.Popen([e.executable,A],cwd=f.getcwd())

def F(t,q=""):
    r=s.get();k=(x("cm93aWQ="),)+C[r]
    [t.delete(i) for i in t.get_children()]
    t["columns"]=k
    [t.heading(i,text=i) or t.column(i,width=120) for i in k]
    try:
        u=c.connect(B);v=u.cursor()
        w=f"SELECT {', '.join(k)} FROM {r}"
        if q:
            z=" OR ".join([f"{i} LIKE ?" for i in k])
            v.execute(w+" WHERE "+z,["%"+q+"%"]*len(k))
        else:v.execute(w)
        y=v.fetchall();u.close()
    except:y=[]
    [t.insert("", "end", values=i, iid=i[0]) for i in y]

def G():F(T,U.get().strip())

def H(i):
    j=s.get();k=(x("cm93aWQ="),)+C[j]
    l=a.Toplevel(R);l.title(x("VXVlbmRh"))
    m=c.connect(B);n=m.cursor()
    n.execute(f"SELECT {', '.join(k)} FROM {j} WHERE rowid=?",(i,))
    o=n.fetchone();m.close()
    if not o:h.showerror(x("VmlnYQ=="),x("UGVhdnVi"));l.destroy();return
    p={}
    for q,r in enumerate(k):
        a.Label(l,text=r).grid(row=q,column=0)
        s_=a.Entry(l,width=40);s_.grid(row=q,column=1)
        s_.insert(0,"" if o[q] is None else o[q]);p[r]=s_
    def Q():
        r_=[p[i].get() for i in k[1:]]
        s1=c.connect(B);t1=s1.cursor()
        u1=", ".join([f"{i}=?" for i in k[1:]])
        t1.execute(f"UPDATE {j} SET {u1} WHERE rowid=?",r_+[i])
        s1.commit();s1.close();F(T);l.destroy();h.showinfo("OK","✔")
    a.Button(l,text="✓",command=Q).grid(row=len(k),column=0,columnspan=2)

def I():
    i=T.selection()
    if not i:h.showwarning("!","?");return
    H(i[0])

R=a.Tk();R.title(x("TWFqdXR1cw=="))

s=a.StringVar(value=D[0])
S=g.Combobox(R,textvariable=s,values=D,state="readonly");S.pack()
S.bind("<<ComboboxSelected>>",lambda e:F(T))

V=a.Frame(R);V.pack(fill="x")
a.Label(V,text=">").pack(side="left")
U=a.Entry(V);U.pack(side="left",expand=1,fill="x")
a.Button(V,text="?",command=G).pack(side="left")

W=a.Frame(R);W.pack(expand=1,fill="both")
X=a.Scrollbar(W);X.pack(side="right",fill="y")
T=g.Treeview(W,yscrollcommand=X.set,show="headings");T.pack(expand=1,fill="both")
X.config(command=T.yview)

Y=a.Frame(R);Y.pack()
a.Button(Y,text="+",command=E).grid(row=0,column=0)
a.Button(Y,text="~",command=I).grid(row=0,column=1)

F(T);R.mainloop()
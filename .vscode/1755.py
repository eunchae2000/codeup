"""
.dib : Paint.Picture  
.doc : Word.Document.8  
.docx : Word.Document.12  
.htm : htmfile  
.html : htmlfile  
.hwp : Hwp.Document.96  
.hwpx : Hwp.Document.hwpx.96  
.hwt : Hwp.Document.hwt.96  
.jpe, .jpeg, .jpg : jpegfile  
.ppt : PowerPoint.Show.8  
.pptx : PowerPoint.Show.12  
.pptxml : powerpointxmlfile
"""

a, b = map(str, input().split("."))

if(b == "dib"):
    print("Paint.Picture")
elif(b == "doc"):
    print("Word.Document.8")
elif(b == "docx"):
    print("Word.Document.12")
elif(b == "htm"):
    print("htmfile")
elif(b == "html"):
    print("htmlfile")
elif(b == "hwp"):
    print("Hwp.Document.96")
elif(b == "hwpx"):
    print("Hwp.Document.hwpx.96")
elif(b == "hwt"):
    print("Hwp.Document.hwt.96")
elif(b == "jpe" or b == "jpeg" or b == "jpg"):
    print("jpegfile")
elif(b == "ppt"):
    print("PowerPoint.Show.8")
elif(b == "pptx"):
    print("PowerPoint.Show.12")
elif(b == "pptxml"):
    print("powerpointxmlfile")
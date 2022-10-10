from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Blog, Congif
from .forms import ContactForm
from py_scripts import test,config, query


def index(request):
    #return HttpResponse("<h1>This message is from Products App</h1>")
    title="Homepage"
    #obj=get_object_or_404(Blog, id=id)
    content={"title":title}
    return render(request, "index.html",content)

def blog_list(request):
    qs= Blog.objects.all()
    template='blog_list.html'
    content={"list":qs}
    return render(request, template, content)

def blog_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        obj= Blog.objects.create(**form.cleaned_data)
        form=ContactForm()
    template='blog_create.html'
    content={"form":form}
    return render(request, template, content)

def blog_detail(request,id):
    obj = get_object_or_404(Blog, id=id)
    template='blog_detail.html'
    content={"object":obj}
    return render(request, template, content)

def blog_update(request,id):
    obj = get_object_or_404(Blog, id=id)
    template='blog_update.html'
    content={"object":obj,"form":None}
    return render(request, template, content)

def blog_delete(request,id):
    obj = get_object_or_404(Blog, id=id)
    template='blog_delete.html'
    content={"object":obj}
    return render(request, template, content)

def about(request):
    env_set = Congif.objects.all();
    env_names = []
    for env_obj in env_set:
        env_names.append({"name": env_obj.env_name, "value": env_obj.env})
    full_query=''
    env=''
    if request.POST.get('query') != None and request.POST.get('query') != '':
        full_query = request.POST.get('query')
    if request.POST.get('environment') != None and request.POST.get('environment') != '':
        env = request.POST.get('environment')
    #print('Query: ', query)
    result=""
    if env != None and env != '':
        obj = get_object_or_404(Congif, env=env)
        print('Env: ',obj.env)
        if full_query!= None and full_query!='':
            result=query.execute_query(full_query, obj)
    if len(result)!=0 and 'error' not in result[0]:
        content = {"header":result[0],"result": result[1], "title": "SQL page", "env_names": env_names,"query":full_query,"env":env}
    else:
        content = {"header": result, "result": result, "title": "SQL page", "env_names": env_names,"query":full_query,"env":env}
    return render(request, "sql.html",content)

def edi(request):
    env_set=Congif.objects.all();
    env_names=[]
    for env_obj in env_set:
        env_names.append({"name":env_obj.env_name,"value":env_obj.env})
    env = request.POST.get('environment')
    bi_id = request.POST.get('bi_id')
    edi_ref = request.POST.get('edi_ref')
    claim = request.POST.get('claim')
    customer = request.POST.get('customer')
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    if end_date!='':
        end_date = end_date;
    else:
        end_date = start_date;
    total = request.POST.get('total-amount')
    submitted = request.POST.get('submitted-amount')
    approved = request.POST.get('approved-amount')
    if env != None and env != '':
        obj = get_object_or_404(Congif, env=env)
    data={"env":env,"bi_id":bi_id, "edi_ref":edi_ref,"claim":claim,"customer":customer,"start_date":start_date,"end_date":end_date,"total":total,"submitted":submitted,"approved":approved}
    print('Data: ', data)
    queries=[]
    message="";
    if claim!=None and claim!='':
        queries=query.generate_query(data,obj)
    if len(queries)!=0:
        if "successfully" in queries[0]:
            message="EDI Bill successfully inserted in DB with BI_ID="+str(queries[1])+" and EDI_REF_NO="+str(queries[2]);
        else:
            message = "EDI Bill insertion failed due to the error " + str(queries[0]);

    content = {"title": "EDI Bill", "env_names": env_names, "message":message}
    return render(request, "edi.html",content)

def multiple_edi(request):
    env_set=Congif.objects.all();
    env_names=[]
    for env_obj in env_set:
        env_names.append({"name":env_obj.env_name,"value":env_obj.env})
    env = request.POST.get('environment')
    count = request.POST.get('count')
    claim = request.POST.get('claim')
    customer = request.POST.get('customer')
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    if end_date!='':
        end_date = end_date;
    else:
        end_date = start_date;
    total = request.POST.get('total-amount')
    submitted = request.POST.get('submitted-amount')
    approved = request.POST.get('approved-amount')
    if env != None and env != '':
        obj = get_object_or_404(Congif, env=env)
    data={"env":env,"count":count,"claim":claim,"customer":customer,"start_date":start_date,"end_date":end_date,"total":total,"submitted":submitted,"approved":approved}
    #print('Data: ', data)
    queries=[]
    message="";
    if claim!=None and claim!='':
        queries=query.generate_multiple_edi(data,obj)
    if len(queries)!=0:
        if "successfully" in queries[0]:
            message=data.get('count')+" EDI Bill(s) inserted successfully  in DB "+str(queries[0]);
        else:
            message = "EDI Bill insertion failed due to the error " + str(queries[0]);

    content = {"title": "Multiple EDI Bill", "env_names": env_names, "message":message,"no_of_bills":"Number of EDI Bills"}
    return render(request, "multiple_edi.html",content)

def multiple_edi_eob(request):
    env_set=Congif.objects.all();
    env_names=[]
    for env_obj in env_set:
        env_names.append({"name":env_obj.env_name,"value":env_obj.env})
    env = request.POST.get('environment')
    count = request.POST.get('count')
    claim = request.POST.get('claim')
    customer = request.POST.get('customer')
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    if end_date!='':
        end_date = end_date;
    else:
        end_date = start_date;
    total = request.POST.get('total-amount')
    submitted = request.POST.get('submitted-amount')
    approved = request.POST.get('approved-amount')
    eob = request.POST.get('eob-amount')
    if env != None and env != '':
        obj = get_object_or_404(Congif, env=env)
    data={"env":env,"count":count,"claim":claim,"customer":customer,"start_date":start_date,"end_date":end_date,"total":total,"submitted":submitted,"approved":approved,"eob":eob}
    #print('Data: ', data)
    queries=[]
    message="";
    if claim!=None and claim!='':
        queries=query.generate_multiple_edi_eob(data,obj)
    if len(queries)!=0:
        if "successfully" in queries[0]:
            message=data.get('count')+" EDI Bill(s) with line item EOB inserted successfully  in DB "+str(queries[0]);
        else:
            message = "EDI Bill insertion failed due to the error " + str(queries[0]);

    content = {"title": "Multiple EDI Bill with EOB", "env_names": env_names, "message":message,"no_of_bills":"Number of EDI Bills"}
    return render(request, "multiple_edi_eob.html",content)

def multiple_line_item(request):
    env_set=Congif.objects.all();
    env_names=[]
    for env_obj in env_set:
        env_names.append({"name":env_obj.env_name,"value":env_obj.env})
    env = request.POST.get('environment')
    count = request.POST.get('count')
    claim = request.POST.get('claim')
    customer = request.POST.get('customer')
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    if end_date!='':
        end_date = end_date;
    else:
        end_date = start_date;
    total = request.POST.get('total-amount')
    submitted = request.POST.get('submitted-amount')
    approved = request.POST.get('approved-amount')
    if env != None and env != '':
        obj = get_object_or_404(Congif, env=env)
    data={"env":env,"count":count,"claim":claim,"customer":customer,"start_date":start_date,"end_date":end_date,"total":total,"submitted":submitted,"approved":approved}
    #print('Data: ', data)
    queries=[]
    message="";
    if claim!=None and claim!='':
        queries=query.generate_multiple_line_item(data,obj)
    if len(queries)!=0:
        if "successfully" in queries[0]:
            message="EDI Bill with "+data.get('count')+" Line Item(s) successfully inserted in DB with BI_ID="+str(queries[1]);
        else:
            message = "EDI Bill insertion failed due to the error " + str(queries[0]);

    content = {"title": "Single EDI Bill with multiple Line item", "env_names": env_names, "message":message,"no_of_bills":"Number of Line Items"}
    return render(request, "multiple_line_item.html",content)

def multiple_line_item_eob(request):
    env_set=Congif.objects.all();
    env_names=[]
    for env_obj in env_set:
        env_names.append({"name":env_obj.env_name,"value":env_obj.env})
    env = request.POST.get('environment')
    count = request.POST.get('count')
    claim = request.POST.get('claim')
    customer = request.POST.get('customer')
    start_date = request.POST.get('start-date')
    end_date = request.POST.get('end-date')
    if end_date!='':
        end_date = end_date;
    else:
        end_date = start_date;
    total = request.POST.get('total-amount')
    submitted = request.POST.get('submitted-amount')
    approved = request.POST.get('approved-amount')
    eob = request.POST.get('eob-amount')
    if env != None and env != '':
        obj = get_object_or_404(Congif, env=env)
    data={"env":env,"count":count,"claim":claim,"customer":customer,"start_date":start_date,"end_date":end_date,"total":total,"submitted":submitted,"approved":approved,"eob":eob}
    #print('Data: ', data)
    queries=[]
    message="";
    if claim!=None and claim!='':
        queries=query.generate_multiple_line_item_eob(data,obj)
    if len(queries)!=0:
        if "successfully" in queries[0]:
            eob_count=int(data.get('count'))*5;
            message = "EDI Bill with " + data.get('count') + " Line Item(s) and "+str(eob_count)+"  EOB item(s) successfully inserted in DB with BI_ID=" + str(queries[1]);
        else:
            message = "EDI Bill insertion failed due to the error " + str(queries[0]);

    content = {"title": "Single EDI Bill with multiple Line item and EOB", "env_names": env_names, "message":message,"no_of_bills":"Number of Line Items"}
    return render(request, "multiple_line_item_eob.html",content)

def contact(request):
    form= ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=ContactForm()
    content = {"title": "Contact page", "form":form}
    return render(request, "form.html", content)
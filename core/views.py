from django.shortcuts import render


def home(request):
    services = [
        {
            "number": "01",
            "title": "فحص وتشخيص الأعطال",
            "description": "فحص واضح للجهاز وتحديد سبب المشكلة قبل بدء أي عملية إصلاح.",
        },
        {
            "number": "02",
            "title": "صيانة الحواسيب المحمولة",
            "description": "معالجة مشاكل الشاشة والبطارية والحرارة ولوحة المفاتيح ومكوّنات الجهاز.",
        },
        {
            "number": "03",
            "title": "ترقية وتحسين الأداء",
            "description": "ترقية الذاكرة والتخزين وتنظيف النظام لتحسين سرعة الجهاز واستقراره.",
        },
    ]

    return render(request, "core/home.html", {"services": services})


def about(request):
    values = [
        {"title": "الوضوح", "text": "نشرح العطل والتكلفة للعميل قبل البدء بالصيانة."},
        {"title": "الاهتمام", "text": "نتعامل مع كل جهاز بعناية ونحافظ على بيانات العميل وخصوصيته."},
        {"title": "الجودة", "text": "نختبر الجهاز بعد الإصلاح للتأكد من أن المشكلة عولجت بشكل صحيح."},
    ]

    return render(request, "core/about.html", {"values": values})

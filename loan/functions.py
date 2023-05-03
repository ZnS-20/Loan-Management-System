from .forms import PersonalSalariedForm, PersonalBusinessForm, HomeBusiness, HomeSalaried, EducationSalaried
from .models import documents


def getFormType(basicDetails):
    return basicDetails.loan_type.type.split(' ')[0]+basicDetails.salary_type.type


def getListofDocuments(formType):
    if formType == "PersonalSalaried":
        return ['address_proof', 'identity_proof', 'passport_photo',
                'salaryslip1', 'salaryslip2', 'salaryslip3']
    elif formType == "PersonalBusiness":
        return ['address_proof', 'identity_proof', 'passport_photo',
                'itr_y1', 'itr_y2', 'itr_y3']
    elif formType == "EducationSalaried":
        return ['address_proof', 'identity_proof', 'passport_photo',
                'high_school_marksheet', 'recommendation_letter', 'proof_of_income']
    elif formType == "HomeSalaried":
        return ['address_proof', 'identity_proof', 'passport_photo',
                'salaryslip_m1', 'salaryslip_m2', 'salaryslip_m2', 'property_doc']
    elif formType == "HomeBusiness":
        return ['address_proof', 'identity_proof', 'passport_photo',
                'itr_y1', 'itr_y2', 'itr_y3', 'property_doc']


def getFormObject(formType, request):
    if request.method == "POST":
        if formType == "PersonalSalaried":
            return PersonalSalariedForm(request.POST, request.FILES)
        elif formType == "PersonalBusiness":
            return PersonalBusinessForm(request.POST, request.FILES)
        elif formType == "EducationSalaried":
            return EducationSalaried(request.POST, request.FILES)
        elif formType == "HomeSalaried":
            return HomeSalaried(request.POST, request.FILES)
        elif formType == "HomeBusiness":
            return HomeBusiness(request.POST, request.FILES)
    else:
        if formType == "PersonalSalaried":
            return PersonalSalariedForm()
        elif formType == "PersonalBusiness":
            return PersonalBusinessForm()
        elif formType == "EducationSalaried":
            return EducationSalaried()
        elif formType == "HomeSalaried":
            return HomeSalaried()
        elif formType == "HomeBusiness":
            return HomeBusiness()


def calculateEMI(principal: float, interest_rate: float, tenure: int, down_payment: float):
    r = (interest_rate/12)/100
    if (down_payment > 0):
        p = principal - ((down_payment/100)*principal)
    else:
        p = principal
    emi = (p*r*((1+r)**tenure))/((1+r)**tenure-1)
    return emi


def setInitialUserDetails(user):
    initial = {
        "first_name": user.user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.user.last_name,
        "email": user.user.email,
        "phone": user.phone,
        "user": user
    }
    return initial


def setBasicDetails(basicDetail, user):
    detail = {
        "loan_type": basicDetail.loan_type,
        "salary_type": basicDetail.salary_type,
        "amount": basicDetail.amount,
        "tenure": basicDetail.tenure,
        "address1": basicDetail.address1,
        "address2": basicDetail.address2
    }
    detail.update(user)
    return detail


def deleteDocuments(basicDetail_id):
    instance = documents.objects.filter(loan_id=basicDetail_id)
    instance.delete()

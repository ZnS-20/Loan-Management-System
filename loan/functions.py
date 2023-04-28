from .forms import PersonalSalariedForm, PersonalBusinessForm, HomeBusiness, HomeSalaried, EducationSalaried


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
    elif formType == "HomeBussiness":
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
        elif formType == "HomeBussiness":
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
        elif formType == "HomeBussiness":
            return HomeBusiness()


def calculateEMI(principal: float, interest_rate: float, tenure: int, down_payment: float):
    r = (interest_rate/12)/100
    emi = (principal*r*((1+r)**tenure))/((1+r)**tenure-1)
    return emi

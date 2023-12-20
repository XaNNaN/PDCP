import numpy as np


class Patient:
    def __init__(self):
        self.gender = None
        self.age = None
        self.bmi = None
        self.arterial_hypertension = False
        self.waist_circum = None
        self.hip_circum = None
        self.glucose = None
        self.triglycerides = None
#        Далее идут индексы на русском без расшифровки за отсутсвием таковой
        self.ot = None
        self.ob = None

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def set_bmi(self, bmi):
        self.bmi = bmi

    def set_arterial_hypertension(self, art_hyp):
        self.arterial_hypertension = art_hyp

    def set_waist_circum(self, waist):
        self.waist_circum = waist

    def set_hip_circum(self, hip):
        self.hip_circum = hip

    def set_glucose(self, glucose):
        self.glucose = glucose

    def set_triglycerides(self, trigl):
        self.triglycerides = trigl

    def set_ot(self, ot):
        self.ot = ot

    def set_ob(self, ob):
        self.ob = ob

    def calculate_tgi(self):
        tr = self.triglycerides * 88.495575
        gl = self.glucose * 18.018018
        return np.log(tr * gl) / 2

    def calculate_p(self):
        tgi = self.calculate_tgi()
        x1 = (0, 1)[self.arterial_hypertension]
        x3 = self.waist_circum / self.hip_circum
        z = 84.824 - 3.590 * x1 - 14.540 * tgi - 13.441 * x3
        p = 1 / (1 + pow(2.7182, -z))
        return p


class PatientBuilder:
    def __init__(self):
        self.patient = Patient()

    def add_gender(self, gender):
        self.patient.set_gender(gender)
        return self

    def add_age(self, age):
        self.patient.set_age(age)
        return self

    def add_bmi(self, bmi):
        self.patient.set_bmi(bmi)
        return self

    def add_arterial_hypertension(self, arterial_hypertension):
        self.patient.set_arterial_hypertension(arterial_hypertension)
        return self

    def add_waist_circum(self, waist_circum):
        self.patient.set_waist_circum(waist_circum)
        return self

    def add_hip_circum(self, hip_circum):
        self.patient.set_hip_circum(hip_circum)
        return self

    def add_glucose(self, glucose):
        self.patient.set_glucose(glucose)
        return self

    def add_triglycerides(self, triglycerides):
        self.patient.set_triglycerides(triglycerides)
        return self

    def add_ot(self, ot):
        self.patient.set_ot(ot)
        return self

    def add_ob(self, ob):
        self.patient.set_ob(ob)
        return self

    def build(self):
        return self.patient


if __name__ == "__main__":
    patient_1 = PatientBuilder() \
                    .add_gender("woman") \
                    .add_age(55) \
                    .add_bmi(27) \
                    .add_waist_circum(87) \
                    .add_hip_circum(113) \
                    .add_glucose(5.2) \
                    .add_triglycerides(1.6) \
                    .build()

    tgi = patient_1.calculate_tgi()
    p = patient_1.calculate_p()
    print("Пациент 1")
    print(f"ИТГ: {round(tgi, 2)}, P: {round(p, 2)}")

    patient_2 = PatientBuilder() \
                    .add_gender("woman") \
                    .add_age(58) \
                    .add_arterial_hypertension(True) \
                    .add_bmi(28.7) \
                    .add_waist_circum(107.4) \
                    .add_hip_circum(97.9) \
                    .add_glucose(9.9) \
                    .add_triglycerides(2.64)\
                    .build()

    tgi = patient_2.calculate_tgi()
    p = patient_2.calculate_p()
    print("Пациент 2")
    print(f"ИТГ: {round(tgi, 2)}, P: {round(p, 2)}")

    patient_3 = PatientBuilder() \
                    .add_gender("woman") \
                    .add_age(60) \
                    .add_arterial_hypertension(True) \
                    .add_bmi(31) \
                    .add_waist_circum(104.1) \
                    .add_hip_circum(107.1) \
                    .add_glucose(5.1) \
                    .add_triglycerides(1.93)\
                    .build()

    tgi = patient_3.calculate_tgi()
    p = patient_3.calculate_p()
    print("Пациент 3")
    print(f"ИТГ: {round(tgi, 2)}, P: {round(p, 2)}")

    patient_4 = PatientBuilder() \
                    .add_gender("man") \
                    .add_age(54) \
                    .add_arterial_hypertension(True) \
                    .add_bmi(27.4) \
                    .add_waist_circum(90.8) \
                    .add_hip_circum(106.1) \
                    .add_glucose(4.8) \
                    .add_triglycerides(1.8)\
                    .build()

    tgi = patient_4.calculate_tgi()
    p = patient_4.calculate_p()
    print("Пациент 4")
    print(f"ИТГ: {round(tgi, 2)}, P: {round(p, 2)}")

    patient_5 = PatientBuilder() \
                    .add_gender("man") \
                    .add_age(56) \
                    .add_arterial_hypertension(True) \
                    .add_bmi(38.9) \
                    .add_waist_circum(135) \
                    .add_hip_circum(120) \
                    .add_glucose(6.6) \
                    .add_triglycerides(1.25)\
                    .build()

    tgi = patient_5.calculate_tgi()
    p = patient_5.calculate_p()
    print("Пациент 5")
    print(f"ИТГ: {round(tgi, 2)}, P: {round(p, 2)}")

    patient_6 = PatientBuilder() \
                    .add_gender("man") \
                    .add_age(54) \
                    .add_arterial_hypertension(True) \
                    .add_bmi(30.4) \
                    .add_waist_circum(105) \
                    .add_hip_circum(106.1) \
                    .add_glucose(5.5) \
                    .add_triglycerides(1.8)\
                    .build()

    tgi = patient_6.calculate_tgi()
    p = patient_6.calculate_p()
    print("Пациент 6")
    print(f"ИТГ: {round(tgi, 2)}, P: {round(p, 2)}")


from django.db import models
from users.models import User
from django.core.validators import MinValueValidator

# Create your models here.

# only one per user
class BackgroundData(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  age = models.IntegerField(validators=[MinValueValidator(18)])
  BP_med = models.IntegerField(null=True, blank=True)
  anticoagulant_med = models.IntegerField(null=True, blank=True)
  chol_med = models.IntegerField(null=True, blank=True)
  hipknee_treat = models.IntegerField(null=True, blank=True)
  lungasthma_med = models.IntegerField(null=True, blank=True)
  longill = models.IntegerField(null=True, blank=True)
  limitact = models.IntegerField(null=True, blank=True)
  effort = models.IntegerField(null=True, blank=True)
  smkevr = models.IntegerField(null=True, blank=True)
  smknow = models.IntegerField(null=True, blank=True)
  mobility = models.IntegerField(null=True, blank=True)
  country = models.IntegerField(null=True, blank=True)
  alcohol = models.IntegerField(null=True, blank=True)
  jointrep = models.IntegerField(null=True, blank=True)
  fractures = models.IntegerField(null=True, blank=True)
  height = models.FloatField(null=True, blank=True)
  bmi = models.FloatField(null=True, blank=True)
  ethnicity = models.IntegerField(null=True, blank=True)
  sex = models.IntegerField(null=True, blank=True)

# potentially many per user
class HealthData(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  background = models.ForeignKey(BackgroundData, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  age = models.IntegerField(validators=[MinValueValidator(18)])
  gait_speed = models.FloatField(null=True, blank=True)
  grip_dom = models.FloatField(null=True, blank=True)
  grip_ndom = models.FloatField(null=True, blank=True)
  FI_ADL = models.FloatField(null=True, blank=True)
  FI_IADL = models.FloatField(null=True, blank=True)
  chair = models.FloatField(null=True, blank=True)
  leg_raise = models.FloatField(null=True, blank=True)
  full_tandem = models.FloatField(null=True, blank=True)
  srh = models.FloatField(null=True, blank=True)
  eye = models.FloatField(null=True, blank=True)
  hear = models.FloatField(null=True, blank=True)
  func = models.FloatField(null=True, blank=True)
  dias = models.FloatField(null=True, blank=True)
  sys = models.FloatField(null=True, blank=True)
  pulse = models.FloatField(null=True, blank=True)
  trig = models.FloatField(null=True, blank=True)
  crp = models.FloatField(null=True, blank=True)
  hdl = models.FloatField(null=True, blank=True)
  ldl = models.FloatField(null=True, blank=True)
  glucose = models.FloatField(null=True, blank=True)
  igf1 = models.FloatField(null=True, blank=True)
  hgb = models.FloatField(null=True, blank=True)
  fib = models.FloatField(null=True, blank=True)
  fer = models.FloatField(null=True, blank=True)
  chol = models.FloatField(null=True, blank=True)
  wbc = models.FloatField(null=True, blank=True)
  mch = models.FloatField(null=True, blank=True)
  hba1c = models.FloatField(null=True, blank=True)
  vitd = models.FloatField(null=True, blank=True)

class SaveData(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  last_question = models.IntegerField(default=0)

class SavedResponse(models.Model):
  save_model = models.ForeignKey(SaveData, on_delete=models.CASCADE)
  variable_id = models.CharField(max_length=20)
  response = models.FloatField()
  type = models.CharField(max_length=12)
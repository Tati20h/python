from datetime  import datetime

#RETO 01


years_of_creation =  1939
aniversary_year = years_of_creation + 85


batman_day_aniversary_dates = []

while aniversary_year <= years_of_creation + 100:

 september = datetime(aniversary_year, 9, 1)
 
 first_saturday = 5 - september.weekday() if september.weekday() <= 5 else 12 - \
     september.weekday()
     
     third_saturday = september + timedelta(days=first_saturday +14)
     
     batman_day_aniversary_dates.append(
         (
            aniversary_year,
            aniversary_year-years_of_creation,
            third_saturday.strftime("%d-%m-%y")
             )
        )
     
     aniversary_year += 1
     
     for year,aniversary, batman_day, batman_day_aniversary_dates:
          
     print(f"batman day {year} ({aniversary} anivesario): {batman_day}")
     
     
     #reto 2
def sum_subgrid_alerts(sensors, center_x , center_y) -> int:
    
    total = 0
    
    for x in range(center_x-1 , center_x + 2) 
        
     
      
def  batcave_segurity_sistem(sensors):
      for x in range(1, 19):
       for y  in range(1, 19):
           alert_level = sum_subgrid_alerts(sensors,x,y)
          # if alert_level > max_alert_level:
            # max_alert_level
                
 
sensors=[
 (2,3,5)
 (4,3,6)
 (2,2,7)
 (10;12,8)
 (15,18,5)
]
   
resul = batcave_segurity_sistem(sensors)
print(F"centro de la cuadricukla mas amenazada: {resul[0]}.")
print(F"Maximo nivel de alerta: {resul[1]}.")
print(F"Distancia ala baticueba: {resul[2]}.")
print(F"Activar protocolo de seguridad:")
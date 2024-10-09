from datetime  import datetime, timedelta

#RETO 01

years_of_creation =  1939
aniversary_year = years_of_creation + 85

batman_day_aniversary_dates = []

while aniversary_year <= years_of_creation + 100:
    september = datetime(aniversary_year, 9, 1)
    first_saturday = 5 - september.weekday() if september.weekday() <= 5 else 12 - \
        september.weekday()
        
    third_saturday = september + timedelta(days=first_saturday + 14)
    batman_day_aniversary_dates.append(
        (
            aniversary_year,
            aniversary_year - years_of_creation,
            third_saturday.strftime("%d-%m-%y")
        )
    )
    aniversary_year += 1
     
for year,aniversary, batman_day in batman_day_aniversary_dates:
    print(f"batman day {year} ({aniversary} anivesario): {batman_day}")
    
#RETO 2
     
def sum_subgrid_alerts(sensors, center_x , center_y) -> int:
    
    total = 0
    
    for x in range(center_x - 1 , center_x + 2): 
        for y in range(center_y - 1, center_y + 2):
          for sensor in sensors:
              if sensor[0] == x and sensor[1] == y:
                  total += sensor[2]

    return total
                  
def batcave_segurity_system(sensors):
    
    max_alert_level: 0
    max_alert_coordinate = (0, 0)
     
    for x in range(1, 19):
       for y  in range(1, 19):
        alert_level = sum_subgrid_alerts(sensors, x, y)
        if alert_level > max_alert_level:
            max_alert_level = alert_level
            max_alert_coordinate = (x, y)
   
    distance = abs(max_alert_coordinate[0]) + abs(max_alert_coordinate[1])
    activate_protocol = max_alert_level > 20
    
    
    return max_alert_level, max_alert_coordinate, distance , activate_protocol
    
sensors=[
    (2, 3, 5),
    (4, 3, 8),
    (2, 2, 7),
    (10, 12, 8),
    (15, 18, 5)
]
   
resul = batcave_segurity_system(sensors)
print(f"centro de la cuadricukla mas amenazada: {resul[0]}.")
print(f"Maximo nivel de alerta: {resul[1]}.")
print(f"Distancia ala baticueba: {resul[2]}.")
print(f"Activar protocolo de seguridad:")
tot_seg = int(input("Digite o total de segundos:"))

dias = tot_seg // 86400

horas_restantes = tot_seg % 86400

horas = horas_restantes // 3600

segundos_restantes = tot_seg % 3600

minutos = segundos_restantes // 60

segundos = segundos_restantes % 60

print(dias, "dias", horas, "horas", minutos, "minutos e ", segundos, "segundos.")

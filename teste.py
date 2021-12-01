import excel

arquivo = Create()
plan1 = arquivo.active_plan
arquivo.set_name(plan1, "First Plan")
arquivo.create_plan("Second Plan")
arquivo.create_set_position("Tird in First")
arquivo.show_plans(arquivo)
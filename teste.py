from excel import main

arquivo = main.inicializate()
plan1 = main.active(arquivo)
plan1 = main.set_name(plan1, 'First Plan')
plan2 = main.create_plan(arquivo, 'Second Plan')
plan3 = main.create_set_position(arquivo, 'Third in First', 0)
main.show_plans(arquivo)
main.insert_cell(plan1, 'A1', 'insert_cell')
main.insert_lines(3, 4, plan1)
main.insert_cell(plan2, 'A2', 7)
main.insert_cell(plan2, 'A3', 1)
main.set_calc(plan2, 'A1', '=SOMA(A2, A3)')
main.read_cell(plan2, 'A1')
main.read_all_lines(plan1)
main.save(arquivo, 'Vai funcionar')
""" main.copy_plan(arquivo, plan1, 'Copied Plan')
main.save(arquivo, 'Vai funcionar dnv') """

from models.connection import Connection

all_elements_query = ("select property.address,  "
					"property.city, "
					"status.name as status_name, "
					"property.price, "
					"property.description "
					"from habi_db.property "
					"inner join status_history on property.id = status_history.property_id "
					"inner join status on status.id = status_history.status_id  "
					"WHERE status.name IN ('pre_venta', 'en_venta', 'vendido') "
					"{filter} "
					"GROUP BY property.id "
					"ORDER BY status_history.update_date DESC;")

class CrudProperties(Connection):
	def all(self):
		data = self.query(all_elements_query.replace('{filter}', ''))
		return data

	def filters(self, params):
		filters_user = ''
		if 'year' in params:
			filters_user = filters_user + "and property.year = '" + params['year'] + "' "
		if 'city' in params:
			filters_user = filters_user + "and property.city = '" + params['city'] + "' "
		if 'status' in params:
			filters_user = filters_user + "and status.name = '" + params['status'] + "' "
		filters_query = all_elements_query.replace('{filter}', filters_user)
		data = self.query(filters_query)
		return data

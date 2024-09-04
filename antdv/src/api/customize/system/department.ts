interface DepartmentTableModel {
  id: string
  parent_id: number
  name: string
  username: string
  description: string
  status: number
  updated_by: number
  updated_time: string
  created_by: number
  created_time: string
  current: number
  pageSize: number
}

type DepartmentTableParams = Partial<Omit<DepartmentTableModel, 'id'>>

export async function getListApi(params?: DepartmentTableParams) {
  return useGet('/department/list', params)
}

export async function upsertApi(params: DepartmentTableModel) {
  return usePost('/department/upsert', params)
}

export type {
  DepartmentTableParams,
  DepartmentTableModel,
}

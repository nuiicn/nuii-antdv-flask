interface UserTableModel {
  id: string
  parent_id: number
  department_id: Department[]
  nickname: string
  username: string
  email: string
  password: string
  login_time: string
  login_status: number
  avatar: string
  status: number
  updated_by: number
  updated_time: string
  created_by: number
  created_time: string
  roles: (string | number)[]
  current: number
  pageSize: number
  column?: string
  value?: string
}

type UserTableParams = Partial<UserTableModel>

interface UserTableColumn {
  dataIndex: keyof UserTableModel
}

interface UpdateTableColumn {
  id: string
  column: string
  value: string
  type: string
}

interface Department {
  id: number
  name: string
  parent_id: number
}

export async function getListApi(params?: UserTableParams) {
  return useGet('/user/list', params)
}

export async function upsertApi(params: UserTableParams) {
  return usePost('/user/upsert', params)
}

export async function updateUserTableColumnApi(params: UpdateTableColumn) {
  return useGet('/user/update-table-column', params)
}

export async function getUsersExcludingCurrentApi(id: string) {
  return useGet('/user/excluding-current', {'id': id})
}


export type {
  UserTableModel,
  UserTableParams,
  UserTableColumn,
  UpdateTableColumn,
}

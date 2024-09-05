<script setup lang="ts">
import type { UnwrapRef } from 'vue'
import { CheckOutlined, EditOutlined } from "@ant-design/icons-vue"
import { cloneDeep } from "lodash-es"
import type { UserTableModel, UserTableColumn, UpdateTableColumn } from '@/api/customize/system/user.ts'
import { getUsersExcludingCurrentApi, updateUserTableColumnApi } from '@/api/customize/system/user.ts'

const props = defineProps<{
  dataSource: UserTableModel[]
  record: UserTableModel
  column: UserTableColumn
}>()

const editableColumn: UnwrapRef<Record<string, UserTableModel | any>> = reactive({})
const selectedColumn = ref()
const usersExcludingCurrent = ref()

const getUsersExcludingCurrent = async (id: string) => {
  try {
    const { data } = await getUsersExcludingCurrentApi(id)
    usersExcludingCurrent.value = data
  }
  catch (e) {
    console.log(e)
  }
}

const updateTableColumn = async (id: string, column: string, value: string, type: string) => {
  try {
    const params: UpdateTableColumn = {
      'id': id,
      'column': column,
      'value': value,
      'type': type,
    }
    const { code } = await updateUserTableColumnApi(params)
    if (code === 200) {
      console.log('success')
    }
  }
  catch (e) {
    console.log(e)
  }
}

const editableColumnEdit = async (id: string, column: string) => {
  if (column === 'parent_id') {
    await getUsersExcludingCurrent(id)
  }
  editableColumn[id] = cloneDeep(props.dataSource.filter(item => id === item.id)[0])
  selectedColumn.value = column
}

const editableColumnSave = async (id: string, column: string, type: string) => {
  await updateTableColumn(id, column, editableColumn[id][column], type)
  Object.assign(props.dataSource.filter(item => id === item.id)[0], editableColumn[id])
  selectedColumn.value = ''
  delete editableColumn[id]
}
</script>
<template>
  <div class="editable-cell">
    <div v-if="editableColumn[record.id] && selectedColumn === column.dataIndex">
      <a-select
        v-if="selectedColumn === 'parent_id'"
        v-model:value="editableColumn[record.id][column.dataIndex]"
        class="editable-cell-select"
        @change="editableColumnSave(record.id, column.dataIndex, 'select')"
      >
        <a-select-option
          v-for="item in usersExcludingCurrent"
          :key="item.id"
          :value="item.username"
        >
          {{ item.username }}
        </a-select-option>
      </a-select>
      <a-input
        v-else
        v-model:value="editableColumn[record.id][selectedColumn]"
        class="editable-cell-input"
        :placeholder="record[column.dataIndex]"
        @pressEnter="editableColumnSave(record.id, selectedColumn, 'input')"
      />
      <check-outlined
        class="editable-cell-icon-check"
        @click="editableColumnSave(record.id, selectedColumn, selectedColumn === 'parent_id' ? 'select' : 'input')"
      />
    </div>
    <div v-else>
      {{ record[column.dataIndex] || '' }}
      <edit-outlined
        class="editable-cell-icon"
        @click="editableColumnEdit(record.id, column.dataIndex)"
      />
    </div>
  </div>
</template>

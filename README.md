# 檔案管理系統後端 Web API
這個檔案管理系統後端 Web API 是一個使用 Web 服務的系統，旨在提供檔案管理的功能。系統的目標是能夠針對每個使用者設定不同的權限，同時也可以透過對群組設定不同的權限來管理使用者。透過將群組中的使用者進行權限的統一控管，減少針對每個使用者單獨設定權限的工作量。

## 功能特色 (Features)
 - 使用者權限管理：能夠針對每個使用者設定不同的權限，包括讀取、寫入、刪除等操作權限。
 - 群組權限管理：支援對群組設定不同的權限，並將群組中的使用者進行權限的統一控管。
 - 統一控管：透過對群組進行權限控管，可以減少對每個使用者進行單獨設定權限的繁瑣工作。
 - Web 介面：提供直觀友好的 Web 介面，方便使用者進行檔案管理操作。
 - 安全性：系統具備安全機制，保障檔案的安全存取，防止未授權的使用者進行非法操作。

## 如何使用 (How to Use)
1. **設定使用者權限**：透過管理介面或 API，設定每個使用者的權限。
2. **建立群組**：建立不同的群組，將相關的使用者加入其中。
3. **設定群組權限**：針對每個群組設定統一的權限。
4. **存取檔案**：使用者通過 API 存取檔案時，系統會根據其所屬的群組和個人權限進行授權。

## API 端點

- **User**
    - /user/token : 取得JWT
    - /user/register : 註冊使用者
    - */user/list_project : 使用者擁有的專案*

- **Project**
    - */project/create_project : 新建專案*
    - */project/rename_project : 重新命名專案*
    - */project/delete_project : 刪除專案*

- **Service**
    - **POST /service/list_dir**：取得目錄列表

更多 API 資訊，請參閱 API 文件。

> 部分功能開發中...

## Database
PostgreSQL

### Table Schema
path
|Column|Type|
|------|----|
|path_id|integer|
|path_name|varchar|
|path_type|integer|

privilege
|Column|Type|
|------|----|
|parent_id|integer|
|child_id|integer|
|user_id|integer|
|privilege|integer|

project
|Column|Type|
|------|----|
|project_id|integer|
|user_id|integer|
|privilege|integer|

users
|Column|Type|
|------|----|
|username|varchar(20)|
|user_id|integer|
|password|varchar|

## 技術細節

- **語言**：使用 **[Python]** 進行開發。
- **框架**：使用 **[FastAPI]** 框架。
- **資料庫**：使用 **[PostgreSQL]** 資料庫進行資料存儲。

## 安裝與配置 (Installation and Configuration)
1. 下載程式碼：
```bash
git clone https://github.com/peterflin/file_system.git
```
2. Run on Docker：
```
docker run -p 8081:8000 --name file_system peterflin/file_system:1.0.0
```

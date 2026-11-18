# Справочник read-only инструментов

Каталог содержит **139 инструментов**. Список формируется из `wb_mcp/server.py` и соответствует MCP-ответу `tools/list`.

Сервер предоставляет только чтение данных Seller API. Инструменты создания, изменения, удаления, публикации, отправки сообщений, управления ценами/ставками/остатками и изменения заказов удалены из каталога, диспетчеризации и HTTP-клиента. HTTP POST используется только там, где сам Wildberries реализовал чтение через POST (например, воронка, поиск и выборки карточек).

Все инструменты магазина поддерживают `shop_id`. Если подключён один магазин, параметр можно не передавать.

## Магазины и диагностика (5)

- `wb_list_shops`
- `wb_degradations`
- `wb_diagnostics`
- `wb_token_info`
- `wb_api_news`

## Карточки и каталог (13)

- `wb_card_errors`
- `wb_cards_list`
- `wb_card_detail`
- `wb_cards_limits`
- `wb_cards_trash`
- `wb_subjects_search`
- `wb_subject_charcs`
- `wb_directory`
- `wb_tags`
- `wb_card_recommendations_get`
- `wb_brands_list`
- `wb_categories_parent`
- `wb_banned_products`

## Цены и акции (13)

- `wb_prices_list`
- `wb_prices_quarantine`
- `wb_prices_upload_status`
- `wb_prices_size_list`
- `wb_promotions_list`
- `wb_promotions_auto`
- `wb_promotions_audit`
- `wb_promotions_details`
- `wb_promotions_products`
- `wb_tariffs_box`
- `wb_tariffs_pallet`
- `wb_tariffs_return`
- `wb_tariffs_commission`

## Реклама и поисковая аналитика (15)

- `wb_advert_list`
- `wb_advert_count`
- `wb_advert_stats`
- `wb_advert_balance`
- `wb_advert_budget`
- `wb_advert_costs`
- `wb_advert_bids_recommendations`
- `wb_advert_clusters`
- `wb_advert_clusters_stats`
- `wb_advert_minus_phrases`
- `wb_advert_payments`
- `wb_advert_subjects`
- `wb_advert_available_nms`
- `wb_search_report`
- `wb_search_texts`

## Заказы, поставки, склады и остатки (41)

- `wb_order_meta_get`
- `wb_orders_status_history`
- `wb_orders_client_info`
- `wb_supplies_reshipment`
- `wb_orders_external_stickers`
- `wb_orders_archive`
- `wb_supply_order_ids`
- `wb_passes_offices`
- `wb_passes_list`
- `wb_supply_trbx_list`
- `wb_supply_trbx_stickers`
- `wb_dbs_orders_new`
- `wb_dbs_orders`
- `wb_dbs_orders_status`
- `wb_dbs_orders_client`
- `wb_dbs_orders_delivery_date`
- `wb_dbs_groups_info`
- `wb_dbs_order_meta_get`
- `wb_cc_orders_new`
- `wb_cc_orders`
- `wb_cc_orders_status`
- `wb_cc_orders_client`
- `wb_cc_order_identity`
- `wb_cc_order_meta_get`
- `wb_fbw_transit_tariffs`
- `wb_warehouse_remains`
- `wb_orders_new`
- `wb_orders_list`
- `wb_orders_status`
- `wb_orders_stickers`
- `wb_supply_detail`
- `wb_supply_barcode`
- `wb_warehouses`
- `wb_supplies_list`
- `wb_stocks_get`
- `wb_fbw_supplies`
- `wb_fbw_supply_detail`
- `wb_fbw_supply_goods`
- `wb_fbw_acceptance_options`
- `wb_fbw_warehouses`
- `wb_acceptance_coefficients`

## Продажи и аналитика (23)

- `wb_analytics_brand_share`
- `wb_analytics_brand_share_brands`
- `wb_analytics_brand_share_parents`
- `wb_analytics_region_sale`
- `wb_analytics_excise`
- `wb_analytics_item_rating`
- `wb_analytics_grouped_history`
- `wb_nm_report`
- `wb_analytics_stocks_sizes`
- `wb_search_table_details`
- `wb_search_table_groups`
- `wb_search_product_orders`
- `wb_jam_subscription`
- `wb_paid_storage`
- `wb_analytics_detail`
- `wb_analytics_history`
- `wb_analytics_stocks`
- `wb_warehouse_remains`
- `wb_analytics_antifraud`
- `wb_analytics_acceptance`
- `wb_stats_sales`
- `wb_stats_orders`
- `wb_stats_stocks`

## Финансы и документы (11)

- `wb_finance_report`
- `wb_finance_reports_list`
- `wb_finance_report_detailed`
- `wb_finance_acquiring_list`
- `wb_finance_acquiring_detailed`
- `wb_deductions`
- `wb_finance_balance`
- `wb_documents_categories`
- `wb_documents_list`
- `wb_document_download`
- `wb_documents_download_bulk`

## Отзывы, вопросы, возвраты и чаты (17)

- `wb_new_feedbacks_questions`
- `wb_feedbacks_archive`
- `wb_feedbacks_pins`
- `wb_feedbacks_pins_count`
- `wb_question_get`
- `wb_feedback_order_return`
- `wb_feedbacks_count_period`
- `wb_questions_count_period`
- `wb_feedbacks_list`
- `wb_feedbacks_count`
- `wb_questions_list`
- `wb_questions_count`
- `wb_returns_list`
- `wb_goods_return_report`
- `wb_buyer_chats`
- `wb_chat_events`
- `wb_chat_download`


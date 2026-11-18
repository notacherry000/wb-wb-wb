"""Regression tests: the MCP catalogue and WB client expose read-only operations only."""

import inspect

from wb_mcp import client as client_module
from wb_mcp import server


WRITE_TOOL_NAMES = {
    "wb_cards_update", "wb_cards_move_to_trash", "wb_cards_recover_from_trash",
    "wb_cards_create", "wb_barcodes_generate", "wb_media_upload",
    "wb_tag_link", "wb_tag_create", "wb_tag_update", "wb_tag_delete",
    "wb_card_recommendations_set", "wb_prices_set", "wb_prices_club_discount",
    "wb_prices_b2b_set", "wb_promotions_add_products", "wb_promotion_exit",
    "wb_advert_create", "wb_advert_deposit", "wb_advert_pause", "wb_advert_start",
    "wb_advert_stop", "wb_advert_delete", "wb_advert_bids_set",
    "wb_advert_cluster_bids", "wb_advert_rename",
    "wb_cards_move_nm", "wb_card_add_nomenclature", "wb_media_upload_file",
    "wb_order_meta_set", "wb_order_meta_delete", "wb_pass_create", "wb_pass_update",
    "wb_pass_delete", "wb_supply_trbx_add", "wb_supply_trbx_delete",
    "wb_dbs_order_action", "wb_dbs_order_meta_set", "wb_dbs_order_meta_delete",
    "wb_cc_order_action", "wb_cc_order_meta_set", "wb_cc_order_meta_delete",
    "wb_feedbacks_pins_set", "wb_feedbacks_pins_delete", "wb_feedbacks_actions",
    "wb_feedback_reply", "wb_question_reply", "wb_return_answer", "wb_chat_send",
    "wb_order_cancel", "wb_supply_create", "wb_supply_add_orders",
    "wb_supply_deliver", "wb_supply_delete", "wb_warehouse_create",
    "wb_warehouse_update", "wb_warehouse_delete", "wb_stocks_update",
    "wb_stocks_delete",
}


def test_write_tools_are_not_registered_or_dispatched():
    registered = {tool.name for tool in server.TOOLS}
    dispatched = (
        set(server.NO_CLIENT_DISPATCH)
        | set(server.CLIENT_DISPATCH)
        | set(server.SHOP_DISPATCH)
    )
    assert not registered & WRITE_TOOL_NAMES
    assert not dispatched & WRITE_TOOL_NAMES
    assert registered == dispatched


def test_read_only_catalogue_has_no_write_parameters():
    for tool in server.TOOLS:
        schema = tool.inputSchema
        assert "norm_queries" not in (schema.get("properties") or {}), tool.name


def test_client_has_no_write_http_helpers_or_mutation_methods():
    cls = client_module.WBClient
    for name in ("_put", "_patch", "_delete"):
        assert not hasattr(cls, name), name
    for name in (
        "cards_update", "cards_move_to_trash", "cards_recover_from_trash",
        "cards_create", "barcodes_generate", "media_save_by_links",
        "tag_nomenclature_link", "tag_create", "tag_update", "tag_delete",
        "card_recommendations_set", "prices_set", "prices_sizes_set",
        "prices_club_discount_set", "prices_b2b_set", "promotions_upload",
        "promotions_exit", "advert_create", "advert_budget_deposit",
        "advert_pause", "advert_start", "advert_stop", "advert_delete",
        "advert_bids_set", "advert_cluster_bids_set", "advert_rename",
        "advert_minus_phrases_set", "cards_move_nm", "card_add_nomenclature",
        "media_upload_file", "order_meta_set", "order_meta_delete",
        "pass_create", "pass_update", "pass_delete", "supply_trbx_add",
        "supply_trbx_delete", "dbs_order_action", "dbs_order_meta_set",
        "dbs_order_meta_delete", "cc_order_action", "cc_order_meta_set",
        "cc_order_meta_delete", "feedbacks_pins_set", "feedbacks_pins_delete",
        "feedbacks_actions", "feedback_reply", "question_reply",
        "returns_claim_answer", "buyer_chat_send", "order_cancel",
        "supply_create", "supply_add_orders", "supply_deliver", "supply_delete",
        "warehouse_create", "warehouse_update", "warehouse_delete",
        "stocks_update", "stocks_delete",
    ):
        assert not hasattr(cls, name), name


def test_minus_phrase_tool_is_read_only():
    tool = next(t for t in server.TOOLS if t.name == "wb_advert_minus_phrases")
    properties = tool.inputSchema["properties"]
    assert set(properties) == {"shop_id", "advert_id", "nm_id"}
    source = inspect.getsource(server._h_advert_minus_phrases)
    assert "advert_minus_phrases_get" in source
    assert "advert_minus_phrases_set" not in source


def test_wb_jam_public_read_api_is_fully_registered():
    expected = {
        "wb_jam_subscription",
        "wb_search_report",
        "wb_search_table_groups",
        "wb_search_table_details",
        "wb_search_texts",
        "wb_search_product_orders",
        "wb_analytics_order_feed",
        "wb_analytics_detail",
        "wb_analytics_history",
        "wb_analytics_grouped_history",
        "wb_analytics_csv_report_create",
        "wb_analytics_csv_reports_list",
        "wb_analytics_csv_report_retry",
        "wb_analytics_csv_report_download",
    }
    registered = {tool.name for tool in server.TOOLS}
    assert expected <= registered
    assert expected <= set(server.CLIENT_DISPATCH)
    assert "wb_nm_report" not in registered


def test_jam_csv_report_types_cover_documented_export_families():
    tool = next(t for t in server.TOOLS if t.name == "wb_analytics_csv_report_create")
    allowed = set(tool.inputSchema["properties"]["report_type"]["enum"])
    assert allowed == {
        "DETAIL_HISTORY_REPORT",
        "GROUPED_HISTORY_REPORT",
        "SEARCH_QUERIES_PREMIUM_REPORT_GROUP",
        "SEARCH_QUERIES_PREMIUM_REPORT_PRODUCT",
        "SEARCH_QUERIES_PREMIUM_REPORT_TEXT",
        "STOCK_HISTORY_REPORT_CSV",
        "STOCK_HISTORY_DAILY_CSV",
    }


def test_jam_csv_report_tools_are_read_workflows_not_seller_mutations():
    client = client_module.WBClient
    for name in (
        "analytics_csv_report_create",
        "analytics_csv_reports_list",
        "analytics_csv_report_retry",
        "analytics_csv_report_download",
        "search_report",
        "search_table_groups",
        "search_table_details",
        "search_texts_by_product",
        "search_product_orders",
        "analytics_sales_funnel",
        "analytics_sales_funnel_history",
        "analytics_sales_funnel_grouped_history",
    ):
        assert hasattr(client, name), name
    assert not hasattr(client, "nm_report")


def test_jam_tools_accept_complete_wb_request_bodies():
    search = next(t for t in server.TOOLS if t.name == "wb_search_report")
    assert "body" in search.inputSchema["properties"]
    texts = next(t for t in server.TOOLS if t.name == "wb_search_texts")
    assert "body" in texts.inputSchema["properties"]
    details = next(t for t in server.TOOLS if t.name == "wb_search_table_details")
    groups = next(t for t in server.TOOLS if t.name == "wb_search_table_groups")
    assert "body" in details.inputSchema["properties"]
    assert "body" in groups.inputSchema["properties"]

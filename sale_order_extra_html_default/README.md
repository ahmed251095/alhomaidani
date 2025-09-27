
# Sale Order Extra HTML Default

- Depends on your existing module **sale_order_extra_images** (which provides `extra_print_html` on `sale.order`).
- Adds a Sales Settings field to store the *default* HTML.
- On creating a new Sales Order, if `extra_print_html` is empty, it is auto-filled from that default.
- No QWeb changes, so it is safe and will not break the web UI.

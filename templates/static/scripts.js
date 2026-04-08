document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', function (e) {
        const row = e.target.closest('tr.table-row-link[data-href]');
        if (!row || e.target.closest('a, button, input, select, textarea')) return;
        window.location.href = row.getAttribute('data-href');
    });
    document.addEventListener('keydown', function (e) {
        if (e.key !== 'Enter' && e.key !== ' ') return;
        const row = e.target.closest('tr.table-row-link[data-href]');
        if (!row || e.target.closest('a, button')) return;
        e.preventDefault();
        window.location.href = row.getAttribute('data-href');
    });

    document.addEventListener('mousedown', function(e) {
        if (e.target.tagName === 'OPTION' && e.target.parentElement.hasAttribute('multiple')) {
            e.preventDefault();
            
            const select = e.target.parentElement;
            const scroll = select.scrollTop;
            
            // Toggle selection
            e.target.selected = !e.target.selected;
            
            // Trigger change event to notify forms
            select.dispatchEvent(new Event('change', { bubbles: true }));
            
            // Keep focus and restore scroll instantly
            select.focus();
            setTimeout(() => {
                select.scrollTop = scroll;
            }, 0);
        }
    });
});

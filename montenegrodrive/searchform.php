<?php
/**
 * Search form
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }
?>
<form role="search" method="get" class="flex gap-2 items-center" action="<?php echo esc_url( home_url( '/' ) ); ?>">
    <label class="screen-reader-text" for="search-<?php echo esc_attr( wp_unique_id() ); ?>">
        <?php esc_html_e( 'Search for:', 'montenegrodrive' ); ?>
    </label>
    <input type="search"
           id="search-<?php echo esc_attr( wp_unique_id() ); ?>"
           class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary bg-surface-container-lowest flex-grow"
           placeholder="<?php esc_attr_e( 'Search…', 'montenegrodrive' ); ?>"
           value="<?php echo esc_attr( get_search_query() ); ?>"
           name="s" />
    <button type="submit" class="bg-primary text-on-primary px-6 h-12 rounded-lg font-label-bold hover:shadow-lg transition-all">
        <?php esc_html_e( 'Search', 'montenegrodrive' ); ?>
    </button>
</form>

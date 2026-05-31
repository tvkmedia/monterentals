<?php
/**
 * Template Name: Elementor Canvas (MontenegroDrive)
 *
 * Use this template when you want Elementor Pro to take over the entire viewport
 * (no theme header, no theme footer). Equivalent to Elementor's built-in
 * "Elementor Canvas" template, but with our enqueued Tailwind + design tokens.
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }
?><!DOCTYPE html>
<html <?php language_attributes(); ?> class="light">
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php wp_head(); ?>
</head>
<body <?php body_class( 'bg-background text-on-background font-body-md antialiased elementor-canvas' ); ?>>
<?php wp_body_open(); ?>

<?php while ( have_posts() ) : the_post(); ?>
    <?php the_content(); ?>
<?php endwhile; ?>

<?php wp_footer(); ?>
</body>
</html>
